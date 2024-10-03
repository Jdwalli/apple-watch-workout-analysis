import axios, { AxiosResponse, AxiosRequestConfig } from "axios";
import {
  ApiClientRequest,
  UploadExportResponse,
  ExportStatusResponse,
} from "../types/client_types";
import { ENDPOINTS } from "../config/apiConstants";

export default class ApiClient {
  private buildAxiosConfig(config: ApiClientRequest): AxiosRequestConfig {
    const axiosConfig: AxiosRequestConfig = {
      method: config.httpMethod,
      url: config.path,
    };

    if (config.queryParams) {
      axiosConfig.params = config.queryParams;
    }

    if (config.body) {
      axiosConfig.data = config.body;
    }

    if (config.headers) {
      axiosConfig.headers = config.headers;
    }

    return axiosConfig;
  }

  async request(config: ApiClientRequest): Promise<AxiosResponse> {
    try {
      const axiosConfig = this.buildAxiosConfig(config);

      const response: AxiosResponse = await axios(axiosConfig);
      return response;
    } catch (error) {
      console.error(error);
      throw error;
    }
  }

  async uploadExport(healthZip: File): Promise<UploadExportResponse> {
    const formData: FormData = new FormData();
    formData.append("file", healthZip);

    try {
      const response = await this.request({
        httpMethod: "POST",
        headers: { "Content-Type": "multipart/form-data" },
        path: ENDPOINTS.UPLOAD,
        body: formData,
      });
      return response.data;
    } catch (error) {
      console.error("Error:", error);
      throw error;
    }
  }

  async dataStatus(): Promise<ExportStatusResponse> {
    try {
      const response = await this.request({
        httpMethod: "GET",
        headers: { "Content-Type": "application/json" },
        path: ENDPOINTS.EXPORT_STATUS,
      });
      return response.data;
    } catch (error) {
      console.error("Error:", error);
      throw error;
    }
  }
}
