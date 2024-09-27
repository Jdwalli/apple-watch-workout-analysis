import React from "react";
import { ThemeProvider } from "@/components/theme-provider";
import Layout from "./components/shared/Layout";
import { Routes, Route } from "react-router-dom";
import ProtectedRoute from "./components/ProtectedRoute";
import { useDispatch, useSelector } from "react-redux";
import { RootState } from "./redux/store";
import { updateExportDataStatus } from "./redux/features/exportDataStatusSlice";

// Pages
import LandingPage from "./pages/landing/LandingPage";
import WorkoutsPage from "./pages/workouts/WorkoutsPage";
import ApiClient from "./clients/api_clients";

function App() {
  const dispatch = useDispatch();
  const apiClient = new ApiClient();
  const exportDataStatus = useSelector(
    (state: RootState) => state.exportDataStatus.exportDataStatus
  );

  React.useEffect(() => {
    const fetchExportDataStatus = async () => {
      try {
        const exportDataStatus = await apiClient.dataStatus();

        dispatch(
          updateExportDataStatus(
            exportDataStatus.exportStatusContext.exportPresent
          )
        );
      } catch (error) {
        console.error("Failed to fetch export data status:", error);
      }
    };

    fetchExportDataStatus();
  });

  return (
    <ThemeProvider defaultTheme="dark" storageKey="vite-ui-theme">
      <Routes>
        <Route path="/" element={<Layout />}>
          <Route index element={<LandingPage />} />
          <Route
            path="/workouts"
            element={
              <ProtectedRoute isAllowed={exportDataStatus} redirectPath="/">
                <WorkoutsPage />
              </ProtectedRoute>
            }
          />
        </Route>
      </Routes>
    </ThemeProvider>
  );
}

export default App;
