import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { ContactsComponent } from './contacts/contacts.component';
import { HomeComponent } from './home/home.component';
import { ArticleListComponent } from './article-list/article-list.component';
import { HttpClientModule } from '@angular/common/http';
import { StudentVideoListComponent } from './student-video-list/student-video-list.component';
import { StudentVideoDetailComponent } from './student-video-detail/student-video-detail.component';
import { ArticleDetailComponent } from './article-detail/article-detail.component';

import { Pipe, PipeTransform } from "@angular/core";
import { DomSanitizer, SafeHtml } from '@angular/platform-browser';

@Pipe({
  name: 'sanitizeHtml'
})
export class SanitizeHtmlPipe implements PipeTransform {

  constructor(private _sanitizer:DomSanitizer) {
  }

  transform(v:string):SafeHtml {
    return this._sanitizer.bypassSecurityTrustHtml(v);
  }
}

@NgModule({
  declarations: [
    AppComponent,
    ContactsComponent,
    HomeComponent,
    ArticleListComponent,
    StudentVideoListComponent,
    StudentVideoDetailComponent,
    ArticleDetailComponent,
    SanitizeHtmlPipe,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
