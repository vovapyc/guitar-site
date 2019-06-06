import { Component, OnInit } from '@angular/core';
import {ActivatedRoute} from "@angular/router";
import {StudentVideosService} from "../student-videos.service";

@Component({
  selector: 'app-student-video-detail',
  templateUrl: './student-video-detail.component.html',
  styleUrls: ['./student-video-detail.component.less']
})
export class StudentVideoDetailComponent implements OnInit {

  studentVideo: any;

  constructor(private studentVideosService: StudentVideosService, private route: ActivatedRoute) {
  }

  ngOnInit() {
    this.route.paramMap.subscribe(params => {
      this.studentVideosService.getStudentVideo(params.get('id')).subscribe(c => {
        this.studentVideo = c;
      })
    });
  }
}
