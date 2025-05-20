import { useState } from "react";
import { useDispatch } from "react-redux";
import searchMeaning from "../../redux/dictionary";
import translateText from "../../redux/translate";


function SearchDictionary() {
    const dispatch = useDispatch();
    const [searchTerm, setSearchTerm] = useState('');
    const [meaning, setMeaning] = useState('');

    const sourceLang = 'en';
    const targetLang = 'es';

    const handleSearch = async () => {
        
        try {
            const data = await dispatch(searchMeaning(searchTerm));
            const text = data.meaning;
            const translation = await dispatch(translateText(text, sourceLang, targetLang));
            setMeaning(translation.translated_text);
        } catch (error) {
            console.error('Translation Failed', error);

            setMeaning('Translation Failed')
        }
        // if (searchTerm) {
        //     setMeaning('Searching...');
        //     fetch(`https://5990bvii05.execute-api.us-east-1.amazonaws.com/dictionary?word=${encodeURIComponent(searchTerm)}`)
        //         .then(response => {
        //             if (!response.ok) {
        //                 throw new Error(`HTTP error! status: ${response.status}`)
        //             }
        //             return response.json();
        //         })
        //         .then( data => {
        //             if (data && data.meaning) {
        //                 setMeaning(data.meaning);
        //             } else if (data && data.word) {
        //                 setMeaning(`Meaning for "${data.word}" not found`);
        //             } else {
        //                 setMeaning('Error retrieving meaning.');
        //             }
        //         })
        //         .catch(error => {
        //             console.error('Error fetching dictionary meaning:', error);
        //             setMeaning('Failed to fetch meaning.')
        //         })
        // } else {
        //     setMeaning('Word')
        // }
    };

    return (
        <div>
            <input
            type="text"
            id="searchInput"
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
            placeholder="Enter Word"
            />
            <button id="searchButton" onClick={handleSearch}>Search</button>
            <div id="meaning ">{meaning}</div>
        </div>
    )
}

export default SearchDictionary;