import { NgModule } from "@angular/core";
import { CommonModule } from "@angular/common";
import { DefaultComponent } from "./default.component";
import { DashboardComponent } from "src/app/modules/dashboard/dashboard.component";
import { RouterModule } from "@angular/router";
import { SharedModule } from "src/app/shared/shared.module";
import {
  MatSidenavModule,
  MatDividerModule,
  MatCardModule,
  MatPaginatorModule,
  MatTableModule,
} from "@angular/material";
import { FlexLayoutModule } from "@angular/flex-layout";
import { DashboardService } from "src/app/modules/dashboard.service";
import { StatisticsComponent } from "src/app/modules/statistics/statistics.component";
import { HomepageComponent } from "../homepage/homepage.component";
import { HttpClientModule } from "@angular/common/http";
import { NgCircleProgressModule } from 'ng-circle-progress';

@NgModule({
  declarations: [
    DefaultComponent,
    DashboardComponent,
    HomepageComponent,
    StatisticsComponent,
  ],
  imports: [
    CommonModule,
    HttpClientModule,
    RouterModule,
    SharedModule,
    MatSidenavModule,
    MatDividerModule,
    FlexLayoutModule,
    MatCardModule,
    MatPaginatorModule,
    MatTableModule,
    NgCircleProgressModule.forRoot({
      // set defaults here
      radius: 100,
      outerStrokeWidth: 16,
      innerStrokeWidth: 8,
      outerStrokeColor: "#78C000",
      innerStrokeColor: "#C7E596",
      animationDuration: 300,
    })
  ],
  providers: [DashboardService],
})
export class DefaultModule {}
