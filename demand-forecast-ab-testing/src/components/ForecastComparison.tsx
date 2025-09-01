import React, { useState } from 'react';
import { ForecastData, ComparisonFilters, ComparisonResult } from '../types/types';
import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend,
  ResponsiveContainer,
} from 'recharts';

interface ForecastComparisonProps {
  data: ComparisonResult[];
  filters: ComparisonFilters;
  onFilterChange: (filters: ComparisonFilters) => void;
}

const ForecastComparison: React.FC<ForecastComparisonProps> = ({
  data,
  filters,
  onFilterChange,
}) => {
  const [selectedMetric, setSelectedMetric] = useState<'mape' | 'rmse' | 'mae'>('mape');

  const renderMetricsTable = () => {
    return (
      <table className="metrics-table">
        <thead>
          <tr>
            <th>Source</th>
            <th>MAPE</th>
            <th>RMSE</th>
            <th>MAE</th>
          </tr>
        </thead>
        <tbody>
          {data.map((result) => (
            <tr key={result.source}>
              <td>{result.source}</td>
              <td>{result.metrics.mape.toFixed(2)}%</td>
              <td>{result.metrics.rmse.toFixed(2)}</td>
              <td>{result.metrics.mae.toFixed(2)}</td>
            </tr>
          ))}
        </tbody>
      </table>
    );
  };

  const renderForecastChart = () => {
    const chartData = data.flatMap((result) =>
      result.forecastData.map((forecast) => ({
        timestamp: forecast.timestamp,
        [`${result.source}_predicted`]: forecast.predictedValue,
        actual: forecast.actualValue,
      }))
    );

    return (
      <ResponsiveContainer width="100%" height={400}>
        <LineChart data={chartData}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="timestamp" />
          <YAxis />
          <Tooltip />
          <Legend />
          {data.map((result) => (
            <Line
              key={result.source}
              type="monotone"
              dataKey={`${result.source}_predicted`}
              stroke={getSourceColor(result.source)}
              name={`${result.source} Forecast`}
            />
          ))}
          <Line
            type="monotone"
            dataKey="actual"
            stroke="#000000"
            name="Actual"
          />
        </LineChart>
      </ResponsiveContainer>
    );
  };

  const getSourceColor = (source: string) => {
    const colors = {
      'vertex-ai': '#4285F4',
      'azure-ml': '#0078D4',
      'databricks': '#FF3621',
    };
    return colors[source as keyof typeof colors] || '#000000';
  };

  return (
    <div className="forecast-comparison">
      <div className="filters">
        <select
          value={filters.family}
          onChange={(e) => onFilterChange({ ...filters, family: e.target.value })}
        >
          <option value="">Select Family</option>
          {/* Add family options dynamically */}
        </select>
        <select
          value={filters.channel}
          onChange={(e) => onFilterChange({ ...filters, channel: e.target.value })}
        >
          <option value="">Select Channel</option>
          {/* Add channel options dynamically */}
        </select>
        <select
          value={filters.dc}
          onChange={(e) => onFilterChange({ ...filters, dc: e.target.value })}
        >
          <option value="">Select DC</option>
          {/* Add DC options dynamically */}
        </select>
      </div>

      <div className="metrics-selector">
        <button
          className={selectedMetric === 'mape' ? 'active' : ''}
          onClick={() => setSelectedMetric('mape')}
        >
          MAPE
        </button>
        <button
          className={selectedMetric === 'rmse' ? 'active' : ''}
          onClick={() => setSelectedMetric('rmse')}
        >
          RMSE
        </button>
        <button
          className={selectedMetric === 'mae' ? 'active' : ''}
          onClick={() => setSelectedMetric('mae')}
        >
          MAE
        </button>
      </div>

      <div className="metrics-table-container">
        {renderMetricsTable()}
      </div>

      <div className="forecast-chart-container">
        {renderForecastChart()}
      </div>
    </div>
  );
};

export default ForecastComparison; 