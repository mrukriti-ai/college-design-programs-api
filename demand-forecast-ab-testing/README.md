# Demand Forecast AB Testing Dashboard

A modern web application for comparing demand forecasts from different ML platforms (Vertex AI, Azure ML, and Databricks) across various dimensions including family, channel, and DC level.

## Features

- Compare forecasts from multiple ML platforms side by side
- Filter data by family, channel, and DC level
- Interactive time series visualization
- Performance metrics comparison (MAPE, RMSE, MAE)
- Date range selection
- Responsive design for all screen sizes

## Prerequisites

- Node.js (v14 or higher)
- npm (v6 or higher)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd demand-forecast-ab-testing
```

2. Install dependencies:
```bash
npm install
```

3. Start the development server:
```bash
npm start
```

The application will be available at `http://localhost:3000`.

## Usage

1. Select the date range for comparison using the date picker in the header
2. Use the filters to select specific family, channel, or DC level
3. View the comparison metrics in the table below
4. Toggle between different metrics (MAPE, RMSE, MAE) using the metric selector buttons
5. Analyze the forecast trends in the interactive chart

## API Integration

To integrate with your actual ML platforms:

1. Update the `fetchData` function in `src/pages/Dashboard.tsx`
2. Replace the mock data with actual API calls to your ML platforms
3. Ensure the response format matches the `ComparisonResult` interface defined in `src/types/types.ts`

## Development

- Built with React and TypeScript
- Uses Recharts for data visualization
- Styled with modern CSS
- Follows responsive design principles

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 