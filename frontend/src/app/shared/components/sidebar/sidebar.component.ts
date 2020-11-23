import { Component, OnInit } from "@angular/core";

@Component({
  selector: "app-sidebar",
  templateUrl: "./sidebar.component.html",
  styleUrls: ["./sidebar.component.scss"],
})
export class SidebarComponent implements OnInit {
  patient_list = [
    "5b891358-1bb3-4bbf-b8a6-a73fbe58efe7",
    "10339b10-3cd1-4ac3-ac13-ec26728cb592",
    "72c0b9ce-7aa4-430b-aaff-bd0ce7846e55",
    "b58731cc-2d8b-4c2d-b327-4cab771af3ef",
    "cfee79fc-df05-476e-b274-43e09ea345db",
    "ad2e9916-4979-40fc-a8c0-68651a0cb5a6",
  ];
  constructor() {}

  ngOnInit() {}
}
