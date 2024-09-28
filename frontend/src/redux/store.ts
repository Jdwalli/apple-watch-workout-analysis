import { configureStore } from "@reduxjs/toolkit";

// Slices
import exportDataStatusSlice from "./features/exportDataStatusSlice";
import exportUploadingStatusSlice from "./features/exportUploadingStatusSlice";
import selectedWorkoutDateSlice from "./features/selectedWorkoutDateSlice";
import selectedWorkoutSlice from "./features/selectedWorkoutSlice";
import workoutLoadingStatusSlice from "./features/workoutLoadingStatusSlice";

export const store = configureStore({
  reducer: {
    selectedWorkoutDate: selectedWorkoutDateSlice,
    exportUploadingStatus: exportUploadingStatusSlice,
    exportDataStatus: exportDataStatusSlice,
    selectedWorkout: selectedWorkoutSlice,
    workoutLoadingStatus: workoutLoadingStatusSlice,
  },
});

export type RootState = ReturnType<typeof store.getState>;
export type AppDispatch = typeof store.dispatch;
