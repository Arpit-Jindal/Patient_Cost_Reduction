import { Component, OnInit } from "@angular/core";

@Component({
  selector: "app-sidebar",
  templateUrl: "./sidebar.component.html",
  styleUrls: ["./sidebar.component.scss"],
})
export class SidebarComponent implements OnInit {
  patient_list = [
    "cae10920-f977-48b4-a0d3-4d70ad561fd1",
    "0042862c-9889-4a2e-b782-fac1e540ecb4",
    "be33d994-f841-40a4-9410-66555cf90fed",
    "b1e9b0b9-da6e-4f68-b603-bd896a50ca86",
    "5c06120a-9af5-4204-951b-7a8bfc465df3",
  ];
  constructor() {}

  ngOnInit() {}
}
