import { useState } from "react";
import axios from "axios";

const topFeatures = [
  {
    name: "Cholesterol LDL_x",
    description: "Niveau de cholestérol LDL en mg/dL",
    unit: "mg/dL"
  },
  {
    name: "Fat (%)",
    description: "Pourcentage de graisses dans l'alimentation",
    unit: "%"
  },
  {
    name: "Carbohydrates (%)",
    description: "Pourcentage de glucides dans l'alimentation",
    unit: "%"
  },
  {
    name: "wit. B2 - Riboflavin",
    description: "Niveau de vitamine B2 (Riboflavine)",
    unit: "mg"
  },
  {
    name: "Vitamin B5 (mg)",
    description: "Niveau de vitamine B5",
    unit: "mg"
  },
  {
    name: "Copper (mg)",
    description: "Niveau de cuivre",
    unit: "mg"
  },
  {
    name: "Zinc (mg)",
    description: "Niveau de zinc",
    unit: "mg"
  },
  {
    name: "Vitamin D (µg)",
    description: "Niveau de vitamine D",
    unit: "µg"
  },
  {
    name: "BMI",
    description: "Indice de masse corporelle",
    unit: "kg/m²"
  },
  {
    name: "Protein_Fat_Ratio",
    description: "Ratio protéines/graisses",
    unit: ""
  },
  {
    name: "Selenium (µg)",
    description: "Niveau de sélénium",
    unit: "µg"
  },
  {
    name: "Manganese (mg)",
    description: "Niveau de manganèse",
    unit: "mg"
  }
];

function App() {
  const [form, setForm] = useState({});
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [errors, setErrors] = useState({});

  const validateInput = (name, value) => {
    if (value < 0) return "La valeur ne peut pas être négative";
    if (name === "BMI" && (value < 10 || value > 50)) return "BMI doit être entre 10 et 50";
    if (name === "Fat (%)" && value > 100) return "Le pourcentage ne peut pas dépasser 100%";
    if (name === "Carbohydrates (%)" && value > 100) return "Le pourcentage ne peut pas dépasser 100%";
    return "";
  };

  const handleChange = (e) => {
    const { name, value } = e.target;
    const numValue = parseFloat(value) || 0;
    const error = validateInput(name, numValue);
    
    setErrors(prev => ({
      ...prev,
      [name]: error
    }));

    setForm(prev => ({
      ...prev,
      [name]: numValue
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    // Vérifier s'il y a des erreurs
    const hasErrors = Object.values(errors).some(error => error !== "");
    if (hasErrors) {
      return;
    }

    setLoading(true);
    try {
      console.log("Envoi des données:", form);
      const res = await axios.post("http://localhost:5000/predict", form);
      console.log("Réponse reçue:", res.data);
      setResult(res.data);
    } catch (err) {
      console.error("Erreur lors de la prédiction:", err);
      setResult({ 
        error: err.response 
          ? `Erreur du serveur: ${err.response.data.error || err.response.statusText}`
          : "Erreur de connexion au serveur. Vérifiez que le serveur Flask est en cours d'exécution."
      });
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-b from-blue-50 to-white p-6">
      <div className="max-w-4xl mx-auto">
        <h1 className="text-4xl font-bold text-center mb-2 text-blue-800">
          🧪 Analyse de Santé
        </h1>
        <p className="text-center text-gray-600 mb-8">
          Entrez vos données pour obtenir une prédiction de santé
        </p>

        <form
          onSubmit={handleSubmit}
          className="grid grid-cols-1 md:grid-cols-2 gap-6 bg-white p-8 rounded-xl shadow-lg"
        >
          {topFeatures.map((feature) => (
            <div key={feature.name} className="space-y-2">
              <label className="block font-medium text-gray-700">
                {feature.name}
                <span className="text-sm text-gray-500 ml-2">({feature.unit})</span>
              </label>
              <input
                type="number"
                name={feature.name}
                step="any"
                onChange={handleChange}
                className={`w-full border rounded-lg p-2 ${
                  errors[feature.name] ? 'border-red-500' : 'border-gray-300'
                } focus:ring-2 focus:ring-blue-500 focus:border-transparent`}
                required
              />
              <p className="text-sm text-gray-500">{feature.description}</p>
              {errors[feature.name] && (
                <p className="text-sm text-red-500">{errors[feature.name]}</p>
              )}
            </div>
          ))}
          
          <button
            type="submit"
            disabled={loading}
            className="md:col-span-2 bg-blue-600 hover:bg-blue-700 text-white font-bold py-3 px-6 rounded-lg transition duration-200 disabled:opacity-50"
          >
            {loading ? (
              <span className="flex items-center justify-center">
                <svg className="animate-spin -ml-1 mr-3 h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                  <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                  <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                </svg>
                Prédiction en cours...
              </span>
            ) : (
              "Obtenir la prédiction"
            )}
          </button>
        </form>

        {result && (
          <div className={`mt-8 p-6 rounded-xl shadow-lg ${
            result.error ? 'bg-red-50' : 'bg-green-50'
          }`}>
            {result.error ? (
              <div className="flex items-center text-red-600">
                <svg className="w-6 h-6 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                </svg>
                <p>{result.error}</p>
              </div>
            ) : (
              <div className="space-y-4">
                <div className="flex items-center">
                  <div className={`p-3 rounded-full ${
                    result.prediction === 1 ? 'bg-green-100' : 'bg-yellow-100'
                  }`}>
                    {result.prediction === 1 ? (
                      <svg className="w-6 h-6 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M5 13l4 4L19 7" />
                      </svg>
                    ) : (
                      <svg className="w-6 h-6 text-yellow-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z" />
                      </svg>
                    )}
                  </div>
                  <div className="ml-4">
                    <h3 className="text-lg font-semibold">
                      {result.prediction === 1 ? "Résultat Positif" : "Résultat Négatif"}
                    </h3>
                    <p className="text-gray-600">
                      Niveau de confiance : {(result.confidence * 100).toFixed(1)}%
                    </p>
                  </div>
                </div>
              </div>
            )}
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
