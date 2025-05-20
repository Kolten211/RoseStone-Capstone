import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { fetchLWDetails, clearWordDetails } from "../../redux/word";
import { useParams } from "react-router-dom";
import './WordDetails.css';
import OpenModalButton from "../OpenModalButton";
import UpdateWord from "../UpdateWord/UpdateWord";




function WordDetails(){
    const dispatch = useDispatch();
    const [loading, setLoading] = useState(true);
    // const location = useLocation()
    // const { learned_word } = location.state
    const { word_id } = useParams();
    
   

    useEffect(() => {
        dispatch(clearWordDetails())
        dispatch(fetchLWDetails(word_id))
        .then(() => setLoading(false))
        .catch(() => setLoading(false))
    }, []);

    const wordInfo = useSelector(state => state.word)
    console.log("Do i have a grip on this now", wordInfo)

    const lw = wordInfo[0];
    console.log("LW", lw)

    if (!wordInfo) return <>Loading...</>

    return (
        <div>
            {loading ? (
                <>Loading...</>
            ) : lw ? (
            <div >
                <h1 className="title">Detalles de la palabra</h1>
                <div className="container">
                    <label>
                        Palabra:
                        <h2 className="border">{lw.word.word}</h2>
                    </label>
                    <label>
                        Translation:
                        {lw.translation ?
                        <h2 className="border"> {lw.translation} </h2>
                        : <h2 className="border">No Translation</h2>}
                    </label>
                    <label>
                        Part of speech:
                        <h2 className="border">{lw.word.part_of_speech}</h2>
                    </label>
                    <h2>Ves algo que falta?</h2>
                    <h2>Haga clic en Agregar detalles.</h2>
                    <OpenModalButton
                        className="Modal-button"
                        buttonText="Add Details"
                        modalComponent={<UpdateWord />}
                    />
                </div>
            </div> ) : <>No Word</>} 
        </div>
    )
}
export default WordDetails