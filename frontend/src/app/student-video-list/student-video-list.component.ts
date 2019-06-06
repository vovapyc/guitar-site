import {Component, OnInit} from '@angular/core';
import {StudentVideosService} from "../student-videos.service";

@Component({
  selector: 'app-student-video-list',
  templateUrl: './student-video-list.component.html',
  styleUrls: ['./student-video-list.component.less']
})
export class StudentVideoListComponent implements OnInit {

  studentVideos: any[] = [];

  constructor(private studentVideosService: StudentVideosService) {
  }

  ngOnInit() {
    this.studentVideosService.getStudentVideos().subscribe((data: any[]) => {
      console.log(data);
      this.studentVideos = data;
    })
  }

}
