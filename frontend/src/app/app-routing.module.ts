import { NgModule } from "@angular/core";
import { Routes, RouterModule } from "@angular/router";
import { AddPatientComponent } from "./add-patient/add-patient.component";
import { DefaultComponent } from "./layouts/default/default.component";
import { HomepageComponent } from "./layouts/homepage/homepage.component";
import { LoginComponent } from "./login/login.component";
import { DashboardComponent } from "./modules/dashboard/dashboard.component";

const routes: Routes = [
  {
    path: "",
    component: LoginComponent,
  },
  {
    path: "dashboard",
    component: DefaultComponent,
    children: [
      {
        path: "",
        component: HomepageComponent,
      },
      {
        path: "patient/:id",
        component: DashboardComponent,
      },
      {
        path: "add",
        component: AddPatientComponent,
      },
    ],
  },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
