import { Component, OnInit } from "@angular/core";
import { DashboardService } from "src/app/modules/dashboard.service";

@Component({
  selector: "app-homepage",
  templateUrl: "./homepage.component.html",
  styleUrls: ["./homepage.component.scss"],
})
export class HomepageComponent implements OnInit {
  bigChart = [];
  cards = [];
  pieChart = [];
  constructor(private dashboardService: DashboardService) {}

  ngOnInit() {
    this.bigChart = this.dashboardService.bigChart();
    this.cards = this.dashboardService.cards();
    this.pieChart = this.dashboardService.pieChart();
  }
}
