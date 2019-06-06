import {Injectable} from '@angular/core';
import {HttpClient} from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class ArticleService {

  API_URL: string = "http://127.0.0.1:8000/api/";

  constructor(private http: HttpClient) {
  }

  getArticles() {
    return this.http.get(this.API_URL + 'posts/')
  }

  getArticle(articleId) {
    return this.http.get(`${this.API_URL + 'posts'}/${articleId}/`)
  }
}
