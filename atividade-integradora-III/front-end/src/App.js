import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useTable } from "react-table";
import MaUTable from "@material-ui/core/Table";
import TableBody from "@material-ui/core/TableBody";
import TableCell from "@material-ui/core/TableCell";
import TableHead from "@material-ui/core/TableHead";
import TableRow from "@material-ui/core/TableRow";
import { Button } from '@material-ui/core';
import Talk from "talkjs";

const columns = [
  {
    Header: "Solicitações recebidas",
    columns: [
      {
        Header: "ID",
        accessor: "id"
      },
      {
        Header: "Descricao",
        accessor: "descricao"
      },
      {
        Header: "usuario",
        accessor: "usuarioNome"
      },
      {
        Header: "Técnico responsavel",
        accessor: "responsavelNome"
      },
    ]
  },
];

function App() {
  const [data, setData] = useState([]);
  const [talkSession, setSession] = useState([]);
  const [me, setUser] = useState([]);

  const user = 1;
  const talkjsContainer = React.createRef();
  const formatSolicitacao = (item) => {
    const numResp = item.atribuicoes_Tecnicos.length
    return {
      ...item,
      usuarioNome: item.usuario.nome,
      responsavelNome: numResp ? item.atribuicoes_Tecnicos[numResp - 1].tecnico.nome : '',
    }
  };
  const baseUrl = 'http://localhost:8000'

  useEffect(() => {
    Talk.ready.then(async () => {
      const result = await axios(
        `${baseUrl}/tecnicos/${user}/`,
      );
      const { id, nome, email } = result.data;
      const funcionario = new Talk.User({
        id,
        name: nome,
        email,
        welcomeMessage: "Hey there! How are you? :-)"
      });
      const session = new Talk.Session({
        appId: "t1gLnbbF",
        me: funcionario,
      });
      setSession(session)
      setUser(funcionario)
    });
  }, []);

  useEffect(() => {
    const fetchData = async () => {
      const result = await axios(
        `${baseUrl}/solicitacoes/?expand=usuario,expand=usuario,atribuicoes_Tecnicos.tecnico`,
      );
      const solicitacoes = result.data.map(item => formatSolicitacao(item));
      setData(solicitacoes);
    };
    fetchData();
  }, []);

  const atribuir = async ({ original: { id } }) => {
    if (id) {
      const resp = await axios.post(
        `${baseUrl}/solicitacoes/${id}/atribuir/`,
        { tecnico: user },
      );
      if (resp.status == 200) {
        data.forEach((item, key) => {
          if (item.id === id) {
            data[key] = formatSolicitacao(resp.data)
          }
        });
        setData(data);
      }
    }
  };
  function openChat({ original: { id } }) {
    const conversation = talkSession.getOrCreateConversation(`solicitacao_${id}`);
    conversation.setParticipant(me);
    const inbox = talkSession.createInbox({ selected: conversation });
    inbox.mount(talkjsContainer.current);

  };
  return (
    <Table columns={columns} data={data} atribuir={atribuir} openChat={openChat.bind(talkSession)} talkjsContainer={talkjsContainer} />
  );
}



const Table = ({ columns, data, atribuir, openChat, talkjsContainer }) => {
  const { getTableProps, headerGroups, rows, prepareRow } = useTable({
    columns,
    data
  });
  return (
    <div>
      <MaUTable {...getTableProps()}>
        <TableHead>
          {headerGroups.map(headerGroup => (
            <TableRow {...headerGroup.getHeaderGroupProps()}>
              {headerGroup.headers.map(column => (
                <TableCell {...column.getHeaderProps()}>
                  {column.render("Header")}
                </TableCell>
              ))}
              <TableCell>Ações</TableCell>
            </TableRow>
          ))}
        </TableHead>
        <TableBody>
          {rows.map((row, i) => {
            prepareRow(row);
            return (
              <TableRow {...row.getRowProps()}>
                {row.cells.map(cell => {
                  return (
                    <TableCell {...cell.getCellProps()}>
                      {cell.render("Cell")}
                    </TableCell>
                  );
                })}
                <TableCell>
                  <Button variant="contained" color="primary" onClick={() => { atribuir(row) }}>Atribuir</Button>
                  <Button variant="contained" color="secondary" onClick={() => { openChat(row) }}>Chat</Button>
                </TableCell>
              </TableRow>
            );
          })}
        </TableBody>
      </MaUTable>
      <div style={{ height: '550px' }} ref={talkjsContainer}></div>
    </div>
  );
};

export default App;
