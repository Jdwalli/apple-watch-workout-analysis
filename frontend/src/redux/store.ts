import { configureStore } from "@reduxjs/toolkit";

// Slices
import selectedWorkoutDateSlice from "./features/selectedWorkoutDateSlice";
import exportUploadingStatusSlice from "./features/exportUploadingStatusSlice";
import exportDataStatusSlice from "./features/exportDataStatusSlice";

export const store = configureStore({
  reducer: {
    selectedWorkoutDate: selectedWorkoutDateSlice,
    exportUploadingStatus: exportUploadingStatusSlice,
    exportDataStatus: exportDataStatusSlice,
  },
});

export type RootState = ReturnType<typeof store.getState>;
export type AppDispatch = typeof store.dispatch;
