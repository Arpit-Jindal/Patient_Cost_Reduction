import { Component, OnInit } from "@angular/core";
import { ActivatedRoute, Params } from "@angular/router";
import { HttpClient } from "@angular/common/http";

@Component({
  selector: "app-dashboard",
  templateUrl: "./dashboard.component.html",
  styleUrls: ["./dashboard.component.scss"],
})
export class DashboardComponent implements OnInit {
  patient_id = "";
  patient_data: any;

  constructor(private http: HttpClient, private route: ActivatedRoute) {}

  ngOnInit() {
    this.route.params.subscribe((params: Params) => {
      this.patient_id = params["id"];
      this.http
        .get("http://127.0.0.1:5000/patient/" + this.patient_id)
        .subscribe((data) => {
          console.log(data);
          this.patient_data = data;
        });
    });
  }
}
