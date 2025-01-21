import { useEffect } from 'react';
import { useNavigate, useParams } from 'react-router-dom';
import { useDispatch, useSelector } from 'react-redux';
import { fetchLessonDetails } from '../../redux/lesson';


function LessonDetails() {
    const { lesson_id } = useParams();
    const dispatch = useDispatch();
    const navigate = useNavigate();
    const sessionUser = useSelector(state = state.session.user);

    useEffect(() => {
        dispatch(fetchLessonDetails
            (lesson_id))
    }, []);


    
}