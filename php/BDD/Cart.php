        <?php
            $servname = 'localhost';
            $dbname = 'pdodb';
            $user = 'root';
            $pass = '';
            
            try{
                $dbco = new PDO("mysql:host=$servname;dbname=$dbname", $user, $pass);
                $dbco->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
                
                $sql = "CREATE TABLE Addres (
                        cartId INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                        userID INTEGER NOT NULL
                        productId INTEGER NOT NULL
                        quantity INTEGER NOT NULL,
                        total float NOT NULL,
                        FOREIGN KEY (userID) REFERENCES Users(userID),
                        FOREIGN KEY (productId) REFERENCES Product(productId)";
                $dbco->exec($sql);
                echo 'Table bien créée !';
            }
            
            catch(PDOException $e){
              echo "Erreur : " . $e->getMessage();
            }
        ?>