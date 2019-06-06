import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { StudentVideoDetailComponent } from './student-video-detail.component';

describe('StudentVideoDetailComponent', () => {
  let component: StudentVideoDetailComponent;
  let fixture: ComponentFixture<StudentVideoDetailComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ StudentVideoDetailComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(StudentVideoDetailComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
