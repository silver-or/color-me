import css from "styled-jsx/css";
import { Button, Col, Form, Row } from "react-bootstrap";
import { useEffect } from "react";
import Link from "next/link";

const Home: React.FC = () => {
  const styled = css`

  `;
  useEffect(() => {
    localStorage.clear();
  });

  return (
    <>
      <div
        id="Fade"
        className="col-md-3 text-center m-auto w-100 p-3"
      >
        퍼스널 컬러 진단
      </div>
    </>
  );
};
export default Home;
