import { all, fork } from 'redux-saga/effects';

import {
  watchReadBestColors,
  watchReadHairs,
  watchReadLips,
  watchReadPersonalColors,
  watchReadPosts,
  watchReadSkins,
  watchReadWorstColors,
  watchReadYoutubers
} from './articleSaga'


// rootSaga를 만들어줘서 store에 추가해주어야 합니다.
export default function* rootSaga() {
  yield all([
    fork(watchReadBestColors),
    fork(watchReadHairs),
    fork(watchReadLips),
    fork(watchReadPersonalColors),
    fork(watchReadPosts),
    fork(watchReadSkins),
    fork(watchReadWorstColors),
    fork(watchReadYoutubers)
  ]);
}