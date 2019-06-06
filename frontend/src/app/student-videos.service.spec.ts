import { TestBed } from '@angular/core/testing';

import { StudentVideosService } from './student-videos.service';

describe('StudentVideosService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: StudentVideosService = TestBed.get(StudentVideosService);
    expect(service).toBeTruthy();
  });
});
