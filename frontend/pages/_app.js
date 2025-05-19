import "@/styles/globals.css";
import {QueryClient, QueryClientProvider, queryOptions} from '@tanstack/react-query';
import {useState} from 'react';
import Layout from "@/components/layout";

// when usemutation, need to Wrap it with queryClientProvider from some reason
export default function App({Component, pageProps}) {
  const [queryClient] = useState(() => new QueryClient());



  return (
    <Layout>
    <QueryClientProvider client={queryClient}>
      <Component {...pageProps} />
    </QueryClientProvider>
    </Layout>
  );
}
