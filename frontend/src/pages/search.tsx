// Frontend: SearchBar.jsx
import { useState, useEffect } from 'react';
import { Search } from 'lucide-react';

interface SearchResult {
  name: string;
  type: 'client' | 'influencer';
}

const SearchBar = () => {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState<SearchResult[]>([]);
  const [isLoading, setIsLoading] = useState(false);

  useEffect(() => {
    const searchItems = async () => {
      if (query.length < 2) {
        setResults([]);
        return;
      }
      setIsLoading(true);
      try {
        const clientResponse = await fetch(`http://127.0.0.1:8000/clients/?search=${query}`);
        const clientData = await clientResponse.json();
        console.log(clientData);
        const clientResults = clientData.map((client: any) => ({
          name: client.name,
          type: 'client'
        }));

        const influencerResponse = await fetch(`http://127.0.0.1:8000/influencers/?search=${query}`);
        const influencerData = await influencerResponse.json();
        const influencerResults = influencerData.map((influencer: any) => ({
          name: influencer.name,
          type: 'influencer'
        }));
        console.log(clientResults.concat(influencerResults));
        setResults(clientResults.concat(influencerResults));
      } catch (error) {
        console.error('Search error:', error);
      } finally {
        setIsLoading(false);
      }
    };

    const debounceTimer = setTimeout(searchItems, 300);
    return () => clearTimeout(debounceTimer);
  }, [query]);

  return (
    <div className="w-full max-w-xl mx-auto">
      <div className="relative">
        <div className="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
          <Search className="h-5 w-5 text-gray-400" />
        </div>
        <input
          type="text"
          className="block w-full pl-10 pr-3 py-2 border border-gray-300 rounded-md leading-5 bg-white placeholder-gray-500 focus:outline-none focus:placeholder-gray-400 focus:ring-1 focus:ring-blue-500 focus:border-blue-500 sm:text-sm"
          placeholder="Search for clients or influencers..."
          value={query}
          onChange={(e) => setQuery(e.target.value)}
        />
        {isLoading && (
          <div className="absolute inset-y-0 right-0 pr-3 flex items-center">
            <div className="animate-spin rounded-full h-4 w-4 border-b-2 border-gray-900"></div>
          </div>
        )}
      </div>
      {results.map((result) => (
        <div key={result.name}>
          {result.name}
          {result.type}
        </div>
      ))}
    </div>
  );
};

export default SearchBar;