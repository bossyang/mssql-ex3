DROP TABLE IF EXISTS dbo.CurrentProductInformation;
DROP TABLE IF EXISTS dbo.HistoricalProductInformation;

CREATE TABLE dbo.CurrentProductInformation (
	ProductId INT NOT NULL,
	Name nvarchar(100) COLLATE Chinese_Taiwan_Stroke_CI_AS NOT NULL,
	Price DECIMAL(9,2) DEFAULT 0.0 NOT NULL,
	PStartDate datetime2 DEFAULT getdate() NOT NULL,
	PEndDate datetime2 DEFAULT '2999-12-31' NOT NULL,
	CONSTRAINT PK_ProductId PRIMARY KEY (ProductId)
);

CREATE SEQUENCE ProductSequence
AS INT
START WITH
1
INCREMENT BY 1;


CREATE TABLE dbo.HistoricalProductInformation (
	ProductId INT NOT NULL,
	Name nvarchar(100) COLLATE Chinese_Taiwan_Stroke_CI_AS NOT NULL,
	Price DECIMAL(9,2) DEFAULT 0.0 NOT NULL,
	PStartDate datetime2 NOT NULL,
	PEndDate datetime2 NOT NULL
);

CREATE NONCLUSTERED INDEX IX_ProductId ON dbo.HistoricalProductInformation ( ProductId ASC );

