import {Component, OnInit} from '@angular/core';
import {ArticleService} from "../article.service";

@Component({
  selector: 'app-article-list',
  templateUrl: './article-list.component.html',
  styleUrls: ['./article-list.component.less']
})
export class ArticleListComponent implements OnInit {

  articles: any[] = [];

  constructor(private articleService: ArticleService) {
  }

  ngOnInit() {
    this.articleService.getArticles().subscribe((data : any[])=>{
        console.log(data);
        this.articles = data;
    })
  }

}
