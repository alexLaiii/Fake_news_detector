import { useState } from 'react';
import { useMutation } from '@tanstack/react-query';
import { Button } from "@/components/ui/button";
import { BookOpenCheckIcon, BrainCogIcon, ChartBarBigIcon, ChartSplineIcon, CircleAlertIcon, CircleXIcon, NewspaperIcon } from 'lucide-react';


export default function Home() {
  const [statement, setStatement] = useState('');
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

   // Create Mutation
   const analyze = useMutation(
    {mutationFn: async () => {
      const res = await fetch('http://localhost:8000/analyze',{
        method: 'POST',
        headers :{'Content-Type': 'application/json'},
        body: JSON.stringify({statement})
      });

      if (!res.ok){
        throw new Error(`Error ${res.status}`);
      }
       return res.json();
    },
    onSuccess: (data) => {
      setResult(data);
      setError(null);
    },
    onError: (err) =>{
      console.log(err);
      setError(err.message);
    },
    onSettled: () =>{
      setLoading(false);
    }

   });

   const handleSubmit = (e) => {
    e.preventDefault();
    setLoading(true);
    analyze.mutate();
   }


return (
  <main className="w-full p-6">


    <div className="max-w-2xl mx-auto space-y-6">
      <h2 className="flex items-center justify-center gap-2 text-3xl font-semibold tracking-tight border-b pb-2">
        <NewspaperIcon className="w-6 h-6" />
        Fake News Detector
      </h2>

      <textarea
        rows={6}
        placeholder="Enter a news statement..."
        value={statement}
        onChange={(e) => setStatement(e.target.value)}
        className="w-full p-3 border rounded-md text-base"
      />

      <Button onClick={handleSubmit}>Analyze</Button>

      {loading && <p className="text-gray-500">Analyzing...</p>}
      {error && <p className="text-red-600">{error}</p>}

      {result && (
        <div className="mt-6 p-5 border rounded-md space-y-3">
          <p className='flex items-center gap-2'><BrainCogIcon/><strong>Prediction:</strong> {" "} {result.label === "fake" ? (
            <span className="flex gap-2 text-red-600 font-bold">Fake<CircleXIcon/></span>
          ) : (
            <span className="flex gap-2 text-blue-600 font-bold">Real<BookOpenCheckIcon/></span>
          )
        
        }</p>
          <p className='flex items-center gap-2'><ChartSplineIcon/><strong> Probability:</strong>{" "} {result.confidence * 100} %</p>
          <p className='flex items-center gap-2'><CircleAlertIcon/><strong> Important words to fact check</strong></p>
          <div className="flex flex-wrap gap-2">
            {result.highlights.map((token, i) => (
              <span key={i} className="">{token}</span>
            ))}
          </div>
          <p className='flex items-center gap-2'><ChartBarBigIcon/><strong> SHAP waterfall plot</strong></p>
          {result.plot_path && (
            <div className="mt-4">
              <img
                src={`http://localhost:8000/${result.plot_path}`}
                alt="SHAP Plot"
                className="max-w-full"
              />
            </div>
          )}
        </div>
      )}
    </div>
  </main>
  );

}
