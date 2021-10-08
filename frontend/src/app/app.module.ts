import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';
import { LandingComponent } from './pages/landing/landing.component';
import { NavigationComponent } from './components/navigation/navigation.component';
import { NavigationButtonComponent } from './components/navigation/navigation-button/navigation-button.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { FooterComponent } from './components/footer/footer.component';
import { SignUpDialogComponent } from './components/dialogs/sign-up-dialog/sign-up-dialog.component';
import { MatDialog, MatDialogModule } from "@angular/material/dialog";
import { Overlay } from "@angular/cdk/overlay";

@NgModule({
  declarations: [
    AppComponent,
    LandingComponent,
    NavigationComponent,
    NavigationButtonComponent,
    FooterComponent,
    SignUpDialogComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FontAwesomeModule,
    BrowserAnimationsModule,
    MatDialogModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
