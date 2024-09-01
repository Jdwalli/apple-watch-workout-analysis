import ApiClient from "./api_client";
import { GetWorkoutsByDateParameters, WorkoutResponse } from "../types/client_types";

export class WorkoutApiClient {
  apiClient = new ApiClient();
  HEADERS = {
    "Content-Type": "application/json"
  }

  async getWorkoutsByDate(params: GetWorkoutsByDateParameters): Promise<WorkoutResponse> {
    try {
      const response = await this.apiClient.request({
        httpMethod: 'POST',
        path: '/api/workout',
        headers: this.HEADERS,
        body: params
      });
      return response.data;
    } catch (error) {
      console.error("Error:", error);
      throw error;
    }
  }


}