import { Component, OnInit } from "@angular/core";

@Component({
  selector: "app-sidebar",
  templateUrl: "./sidebar.component.html",
  styleUrls: ["./sidebar.component.scss"],
})
export class SidebarComponent implements OnInit {
  patient_list = [
    "128d5c93-dfce-49a1-8d08-e9b24abcb4db",
    "0042862c-9889-4a2e-b782-fac1e540ecb4",
    "cae10920-f977-48b4-a0d3-4d70ad561fd1",
    "756e459c-b53e-4120-b427-a80a5caebc06",
    "33454fc9-b2ea-407a-9a9d-64897cf44093",
    "be33d994-f841-40a4-9410-66555cf90fed",
    "bb30c9d3-913c-49ce-8cd9-75405f7a19e9",
    "b1e9b0b9-da6e-4f68-b603-bd896a50ca86",
    "0149d553-f571-4e99-867e-fcb9625d07c2",
    "5c06120a-9af5-4204-951b-7a8bfc465df3",
  ];
  constructor() {}

  ngOnInit() {}
}
