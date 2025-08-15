const config = {
  development: {
    apiUrl: 'http://localhost:8000'
  },
  production: {
    apiUrl: process.env.NEXT_PUBLIC_API_URL || 'https://your-fake-news-detector-backend.herokuapp.com'
  }
};

const environment = process.env.NODE_ENV || 'development';
export const apiUrl = config[environment].apiUrl; 