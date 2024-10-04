CREATE TABLE IF NOT EXISTS "Clients" (
	"Client_ID" INTEGER NOT NULL UNIQUE,
	"Nom" VARCHAR,
	"Prenom" VARCHAR,
	"Email" VARCHAR,
	"Telephone" VARCHAR,
	"Date_Naissance" DATE,
	"Adresse" BLOB,
	"Consentement_Marketing" BOOLEAN,
	PRIMARY KEY("Client_ID"),
	FOREIGN KEY ("Client_ID") REFERENCES "Commandes"("Client_ID")
	ON UPDATE CASCADE ON DELETE RESTRICT
);

CREATE TABLE IF NOT EXISTS "Commandes" (
	"Commande_ID" INTEGER NOT NULL UNIQUE,
	"Date_Commande" DATETIME NOT NULL,
	"Montant_Commande" NUMERIC,
	"Client_ID" INTEGER NOT NULL,
	PRIMARY KEY("Commande_ID", "Client_ID")
);
