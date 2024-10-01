db.filmes.createIndex({ titulo: "text" });
db.avaliacoes.createIndex({ usuarioId: "hashed" });
