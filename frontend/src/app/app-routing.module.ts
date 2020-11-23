import { NgModule } from "@angular/core";
import { Routes, RouterModule } from "@angular/router";
import { DefaultComponent } from "./layouts/default/default.component";
import { HomepageComponent } from "./layouts/homepage/homepage.component";
import { DashboardComponent } from "./modules/dashboard/dashboard.component";
import { StatisticsComponent } from "./modules/statistics/statistics.component";

const routes: Routes = [
  {
    path: "",
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
        path: "stats",
        component: StatisticsComponent,
      },
    ],
  },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
