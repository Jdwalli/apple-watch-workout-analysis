import { createSlice, PayloadAction } from "@reduxjs/toolkit";
import { ExportUploadingStatus } from "../types";

const initialState: ExportUploadingStatus = {
  exportUploadingStatus: false,
};

export const exportUploadingStatusSlice = createSlice({
  name: "exportUploadingStatus",
  initialState: initialState,
  reducers: {
    updateExportUploadingStatus: (state, action: PayloadAction<boolean>) => {
      state.exportUploadingStatus = action.payload;
    },

    resetExportUploadingStatus: (state) => {
      state.exportUploadingStatus = false;
    },
  },
});

export const { updateExportUploadingStatus, resetExportUploadingStatus } =
  exportUploadingStatusSlice.actions;

export default exportUploadingStatusSlice.reducer;
