import React, { useState, useEffect } from 'react';
import ForecastComparison from '../components/ForecastComparison';
import { ComparisonFilters, ComparisonResult } from '../types/types';

const Dashboard: React.FC = () => {
  const [filters, setFilters] = useState<ComparisonFilters>({
    dateRange: {
      start: new Date(Date.now() - 30 * 24 * 60 * 60 * 1000).toISOString().split('T')[0],
      end: new Date().toISOString().split('T')[0],
    },
    sources: ['vertex-ai', 'azure-ml', 'databricks'],
  });

  const [comparisonData, setComparisonData] = useState<ComparisonResult[]>([]);

  useEffect(() => {
    // TODO: Replace with actual API call
    const fetchData = async () => {
      try {
        // Mock data for demonstration
        const mockData: ComparisonResult[] = [
          {
            source: 'vertex-ai',
            metrics: {
              mape: 12.5,
              rmse: 150.3,
              mae: 120.8,
            },
            forecastData: [],
          },
          {
            source: 'azure-ml',
            metrics: {
              mape: 13.2,
              rmse: 155.7,
              mae: 125.4,
            },
            forecastData: [],
          },
          {
            source: 'databricks',
            metrics: {
              mape: 11.8,
              rmse: 145.2,
              mae: 118.6,
            },
            forecastData: [],
          },
        ];
        setComparisonData(mockData);
      } catch (error) {
        console.error('Error fetching comparison data:', error);
      }
    };

    fetchData();
  }, [filters]);

  return (
    <div className="dashboard">
      <header className="dashboard-header">
        <h1>Demand Forecast AB Testing Dashboard</h1>
        <div className="date-range-picker">
          <input
            type="date"
            value={filters.dateRange.start}
            onChange={(e) =>
              setFilters({
                ...filters,
                dateRange: { ...filters.dateRange, start: e.target.value },
              })
            }
          />
          <span>to</span>
          <input
            type="date"
            value={filters.dateRange.end}
            onChange={(e) =>
              setFilters({
                ...filters,
                dateRange: { ...filters.dateRange, end: e.target.value },
              })
            }
          />
        </div>
      </header>

      <main className="dashboard-content">
        <ForecastComparison
          data={comparisonData}
          filters={filters}
          onFilterChange={setFilters}
        />
      </main>
    </div>
  );
};

export default Dashboard; 