import { BrowserModule } from "@angular/platform-browser";
import { NgModule } from "@angular/core";

import { AppRoutingModule } from "./app-routing.module";
import { AppComponent } from "./app.component";
import { BrowserAnimationsModule } from "@angular/platform-browser/animations";
import { DefaultModule } from "./layouts/default/default.module";
import { HttpClientModule } from "@angular/common/http";
import { LoginComponent } from "./login/login.component";
import { MatButtonModule } from "@angular/material";
import { FormsModule } from "@angular/forms";
@NgModule({
  declarations: [AppComponent, LoginComponent],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    DefaultModule,
    MatButtonModule,
    FormsModule,
  ],
  providers: [HttpClientModule],
  bootstrap: [AppComponent],
})
export class AppModule {}
