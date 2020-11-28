import { Component, OnInit } from "@angular/core";
import { NgForm } from "@angular/forms";
import { Router } from "@angular/router";

@Component({
  selector: "app-login",
  templateUrl: "./login.component.html",
  styleUrls: ["./login.component.scss"],
})
export class LoginComponent implements OnInit {
  constructor(private router: Router) {}

  ngOnInit() {}
  onSubmit(form: NgForm) {
    const username = form.value.username;
    const password = form.value.password;

    if (username == "admin" && password == "admin123@") {
      this.router.navigate(["dashboard"]);
    } else {
      alert("Incorrect Credentials");
    }
  }
}
