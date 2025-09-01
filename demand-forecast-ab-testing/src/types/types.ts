export interface ForecastData {
  id: string;
  timestamp: string;
  family: string;
  channel: string;
  dc: string;
  predictedValue: number;
  actualValue?: number;
  confidenceInterval: {
    lower: number;
    upper: number;
  };
  source: 'vertex-ai' | 'azure-ml' | 'databricks';
  metrics: {
    mape: number;
    rmse: number;
    mae: number;
  };
}

export interface ComparisonFilters {
  family?: string;
  channel?: string;
  dc?: string;
  dateRange: {
    start: string;
    end: string;
  };
  sources: ('vertex-ai' | 'azure-ml' | 'databricks')[];
}

export interface ComparisonResult {
  source: string;
  metrics: {
    mape: number;
    rmse: number;
    mae: number;
  };
  forecastData: ForecastData[];
} 