import { Article, ArticleState } from "@/modules/types";
import { createSlice, PayloadAction } from "@reduxjs/toolkit";

export class ArticleService {
  public createArticleSlice() {
    const initialState: ArticleState = {
      data: {
        id: 1,
        title: "",
        content: "",
        open: "",
        picture: null,
        writtenDate: "",
        pictureName: "",
      },
      status: "loading",
      error: null,
    };
    return {
      name: "articleSlice",
      initialState,
      reducers: {
        writeArticle: (state: any, action: PayloadAction<Article>) => {
          alert(`게시글 작성 액션 요청`);
          console.log(action);
          state.data = action.payload;
          state.status = "loading";
          console.log(
            `게시글 작성 성공 - 리듀서 ${JSON.stringify(state.data)}`
          );
        },

        // 서버 갔다 온 액션
        readBestColorsSuccess: (state: any, action: PayloadAction) => {
          state.status = "successed";
        },
        readBestColorsFailure: (state: any, action: PayloadAction) => {
          alert(`best colors 데이터 읽어오기 실패`);
          state.status = "failed";
        },

        readHairsSuccess: (state: any, action: PayloadAction) => {
          state.status = "successed";
        },
        readHairsFailure: (state: any, action: PayloadAction) => {
          alert(`hairs 데이터 읽어오기 실패`);
          state.status = "failed";
        },

        readLipsSuccess: (state: any, action: PayloadAction) => {
          state.status = "successed";
        },
        readLipsFailure: (state: any, action: PayloadAction) => {
          alert(`lips 데이터 읽어오기 실패`);
          state.status = "failed";
        },

        readPersonalColorsSuccess: (state: any, action: PayloadAction) => {
          state.status = "successed";
        },
        readPersonalColorsFailure: (state: any, action: PayloadAction) => {
          alert(`personal colors 데이터 읽어오기 실패`);
          state.status = "failed";
        },

        readPostsSuccess: (state: any, action: PayloadAction) => {
          state.status = "successed";
        },
        readPostsFailure: (state: any, action: PayloadAction) => {
          alert(`posts 데이터 읽어오기 실패`);
          state.status = "failed";
        },

        readSkinsSuccess: (state: any, action: PayloadAction) => {
          state.status = "successed";
        },
        readSkinsFailure: (state: any, action: PayloadAction) => {
          alert(`skins 데이터 읽어오기 실패`);
          state.status = "failed";
        },

        readWorstColorsSuccess: (state: any, action: PayloadAction) => {
          state.status = "successed";
        },
        readWorstColorsFailure: (state: any, action: PayloadAction) => {
          alert(`worst colors 데이터 읽어오기 실패`);
          state.status = "failed";
        },

        readYoutubersSuccess: (state: any, action: PayloadAction) => {
          state.status = "successed";
        },
        readYoutubersFailure: (state: any, action: PayloadAction) => {
          alert(`youtubers 데이터 읽어오기 실패`);
          state.status = "failed";
        },

      /*
        fetchArticles: (state: any) => {
          console.log(`게시글 불러오기 - 리듀서`);
          state.status = "loading";
        },
        fetchArticleSuccess: (state: any, { payload }: any) => {
          state.data = payload;
          state.status = "successed";
          console.log(
            `게시글 불러오기 성공 - 리듀서 ${JSON.stringify(state.data)}`
          );
        },
        fetchArticleFailure: (state: any, { payload }: any) => {
          console.log(`게시글 불러오기 실패 - 리듀서`);
          state.error = payload;
          state.status = "failed";
        },
        fetchMyArticle: (state: any, action: PayloadAction<Article>) => {
          console.log(action);
          state.data = action.payload;
          state.status = "loading";
          console.log(`내 게시물 분류 과정 ${JSON.stringify(state.data)}`);
        },
        fetchMyArticleSuccess: (state: any, action: PayloadAction<Article>) => {
          console.log(action);
          state.data = action.payload;
          state.status = "successed";
          console.log(`게시물 받아오기 성공 ${JSON.stringify(state.data)}`);
        },
        fetchMyArticleFailure: (state: any, action: PayloadAction) => {
          console.log(action);
          state.status = "failed";
        },
        removeArticle: (state: any, action: PayloadAction<Article>) => {
          console.log(`게시글 삭제하기 - 리듀서`);
          state.status = "loading";
          state.data = action.payload;
        },
        writeComment: (state: any, action: PayloadAction<Article>) => {
          console.log(`댓글 등록`);
          state.status = "loading";
          state.data = action.payload;
        },
        commentSuccess: (state: any, action: PayloadAction<Article>) => {
          console.log(`댓글 등록 성공`);
          state.status = "successed";
          state.data = action.payload;
        },
        commentFailure: (state: any, action: PayloadAction) => {
          console.log(`댓글 등록 실패`);
          state.status = "failed";
        },
      */
      },
    };
  }
}
