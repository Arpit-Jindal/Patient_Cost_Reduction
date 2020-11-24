import { Component, OnInit, Input, ChangeDetectorRef } from '@angular/core';
import * as Highcharts from 'highcharts';
import HC_exporting from 'highcharts/modules/exporting';


@Component({
  selector: 'app-widget-area',
  templateUrl: './area.component.html',
  styleUrls: ['./area.component.scss']
})
export class AreaComponent implements OnInit {

  chartOptions: {};
  @Input() data: any = {};

  Highcharts = Highcharts;

  constructor(private ref: ChangeDetectorRef) { }


  ngOnInit() {
    this.chartOptions = {
      chart: {
        type: 'line'
    },
    title: {
        text: this.data.name
    },

    xAxis: {
      title:{
        text: 'Last 2 weeks',
      }
    },
    
    plotOptions: {
        line: {
            dataLabels: {
                enabled: false
            },
            enableMouseTracking: false
        }
    },
    series: [{
          name: 'Patient',
          data: this.data.plots.Patient.slice(0,14)
      }, {
          name: 'Healthy Human',
          data: this.data.plots.Normal.slice(0,14)
      }]
    };
    HC_exporting(Highcharts);

    setTimeout(() => {
      window.dispatchEvent(
        new Event('resize')
      );
    }, 300);
  }

}
