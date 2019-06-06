import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { StudentVideoListComponent } from './student-video-list.component';

describe('StudentVideoListComponent', () => {
  let component: StudentVideoListComponent;
  let fixture: ComponentFixture<StudentVideoListComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ StudentVideoListComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(StudentVideoListComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
