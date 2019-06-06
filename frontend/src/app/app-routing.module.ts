import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { ContactsComponent } from "./contacts/contacts.component";
import {HomeComponent} from "./home/home.component";
import {ArticleListComponent} from "./article-list/article-list.component";
import {ArticleDetailComponent} from "./article-detail/article-detail.component";
import {StudentVideoListComponent} from "./student-video-list/student-video-list.component";
import {StudentVideoDetailComponent} from "./student-video-detail/student-video-detail.component";

const routes: Routes = [
  {path: '', component: HomeComponent},
  {path: 'contacts', component: ContactsComponent},
  {path: 'articles', component: ArticleListComponent},
  {path: 'article/:id', component: ArticleDetailComponent},
  {path: 'student-videos', component: StudentVideoListComponent},
  {path: 'student-video/:id', component: StudentVideoDetailComponent},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
