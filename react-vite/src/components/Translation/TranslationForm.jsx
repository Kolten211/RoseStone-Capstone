import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux"
import translateText from "../../redux/translate";

// const applyCustomSpelling = (translatedText, customSpellings) => {
//     let output = translatedText;

//     for (const [originalWord, customSpelling] of Object.entries(customSpellings)) {
//         const regex = new RegExp(`\\b${originalWord}\\b`, 'gi');
//         output = output.replace(regex, customSpelling);
//     }
//     return output
// }


const Translator = () => {
    const dispatch = useDispatch();
    const [ text,  setText ] = useState('');
    const [ sourceLang, setSourceLang ] = useState('es');
    const [ targetLang, setTargetLang ] = useState('en');
    const [ translatedText, setTranslatedText ] = useState('');
    // const translatedData = useSelector(state => state.translation)
    // const customSpellings = {
    //     "color": "culr"
    // }

    const handleTranslate = async () => {
        console.log("Dispatch", dispatch)
        try{
            const data = await dispatch(translateText(text, sourceLang, targetLang));
            console.log("DATA", data)
            setTranslatedText(data.translated_text);

            // const customText = applyCustomSpelling(data.translated_text, customSpellings);

            // setTranslatedText(customText);

        } catch (error) {
            console.error('Translation Failed', error);

            setTranslatedText('Translation Failed')
        }
    }

    // useEffect(() => {
    //     if (translatedData && translatedData.translated_text) {
    //         setTranslatedText(translatedData.translated_text);
    //     }
    // }, []);

    // const handleAddWord = async () => {
        
    // }

    return (
        <div>

            <input
            type='text'
            value={text}
            onChange={(e) => setText(e.target.value)}
            placeholder="Ingresa tu palabra"
            />

            <select
            value={sourceLang}
            onChange={(e) => setSourceLang(e.target.value)}
            >
                <option value='es'>Español</option>
                <option value="en">Engles</option>
            </select>

            <select
            value={targetLang}
            onChange={(e) => setTargetLang(e.target.value)}
            >
                <option value='en'>Engles</option>
                <option value='es'>Español</option>
            </select>

            <button onClick={handleTranslate}>Traducir</button>

            <p>Translated Text: {translatedText}</p>

            {/* <button onClick={} disabled={!translateText}>
                
            </button> */}
        </div>
    )
}


export default Translator