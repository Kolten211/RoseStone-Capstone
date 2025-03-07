import { useDispatch } from "react-redux"
import { removeWord } from "../../redux/word";
import { useModal } from "../../context/Modal";
import "./DeleteWord.css";


function DeleteWords({ word }) {
    const dispatch = useDispatch();
    const { closeModal } = useModal();

    const handleDelete = () => {
        dispatch(removeWord(word.id))
        closeModal()
    };

    const handleKeep = () => {
        closeModal()
    }

    return (
        <div className="delete-modal">
            <h2>Confirm Delete</h2>
            <p>Are you sure you want to remove this Word?</p>
            <div className="Words-buttons">
                <button onClick={handleDelete}>YES(Delete Words)</button>
                <button onClick={handleKeep} className="grayButton">No(Keep Words)</button>
            </div>
        </div>
    )
}

export default DeleteWords