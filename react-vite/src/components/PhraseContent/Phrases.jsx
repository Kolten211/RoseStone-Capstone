import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { fetchLearnedPhrases } from "../../redux/phrase";
import { NavLink } from "react-router-dom";
import OpenModalButton from "../OpenModalButton";
import DeletePhrase from "../DeletePhrase/DeletePhrase";

function PhraseTile({ learned_phrase }) {
    return (
        <div>
            <NavLink to={`/learned/${learned_phrase.id}/details`} state={{ learned_phrase }} className="phrase-link">
                <div>{learned_phrase.phrases}</div>
            </NavLink>
            <OpenModalButton
            buttonText='Delete'
            modalComponent={<DeletePhrase phrase={learned_phrase}/>}
            />
        </div>
    )
}
function LearnedPhrases() {
    const dispatch = useDispatch();
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        dispatch(fetchLearnedPhrases())
        .then(() => setLoading(false))
        .catch(() => setLoading(false))
    }, []);

    const learned = useSelector(state => state.phrse)
    console.log("PLease", learned)

    return (
        <>
        <div>
            <h1>la frase</h1>
            <h3>Practícalos con frecuencia</h3>
            <h4>Aprende la frase</h4>
                <a href="https://www.ingles.com/" target="_blank"  rel="noreferrer" className="link"> Ingles.com</a>
        </div>
        <div>
            { loading ? (
                <>Loading...</>
            ) : learned && learned[0]?.phrases ? (
                learned[0].phrases?.map(lp => (
                    <PhraseTile key={lp.id} learned_phrase={lp}/>
                ))
            ) : (
                <>No frase</>
            )}
        </div>
        </>
    )
}

export default LearnedPhrases