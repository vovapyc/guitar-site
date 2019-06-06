import {Injectable} from '@angular/core';
import {HttpClient} from "@angular/common/http";

@Injectable({
  providedIn: 'root'
})
export class StudentVideosService {
  API_URL: string = "http://127.0.0.1:8000/api/";

  constructor(private http: HttpClient) {
  }

  getStudentVideos() {
    return this.http.get(this.API_URL + 'student-videos/')
  }

  getStudentVideo(studentVideoId) {
    return this.http.get(`${this.API_URL + 'student-videos'}/${studentVideoId}/`)
  }
}
