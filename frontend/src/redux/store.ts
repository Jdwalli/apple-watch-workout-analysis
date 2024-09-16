import { configureStore } from "@reduxjs/toolkit";

// Slices
import selectedWorkoutDateSlice from "./features/selectedWorkoutDateSlice";

export const store = configureStore({
  reducer: {
    selectedWorkoutDate: selectedWorkoutDateSlice,
  },
});

export type RootState = ReturnType<typeof store.getState>;
export type AppDispatch = typeof store.dispatch;