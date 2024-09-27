export interface SelectedWorkoutDate {
  selectedWorkoutDate: string | undefined;
}

export interface ExportUploadingStatus {
  exportUploadingStatus: boolean;
}

export interface ExportDataStatus {
  exportDataStatus: boolean;
}

export interface RootState {
  selectedWorkoutDate: SelectedWorkoutDate;
}

export interface Action {
  type: string;
  payload: any;
}
