import { createSlice, PayloadAction } from "@reduxjs/toolkit";
import { ExportDataStatus } from "../types";

const initialState: ExportDataStatus = {
  exportDataStatus: false,
};

export const exportDataStatusSlice = createSlice({
  name: "exportDataStatus",
  initialState: initialState,
  reducers: {
    updateExportDataStatus: (state, action: PayloadAction<boolean>) => {
      state.exportDataStatus = action.payload;
    },

    resetExportDataStatus: (state) => {
      state.exportDataStatus = false;
    },
  },
});

export const { updateExportDataStatus, resetExportDataStatus } =
  exportDataStatusSlice.actions;

export default exportDataStatusSlice.reducer;
