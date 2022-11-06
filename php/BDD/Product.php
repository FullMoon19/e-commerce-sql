         <?php
            $servname = 'localhost';
            $dbname = 'pdodb';
            $user = 'root';
            $pass = '';
            
            try{
                $dbco = new PDO("mysql:host=$servname;dbname=$dbname", $user, $pass);
                $dbco->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
                
                $sql = "CREATE TABLE Product(
                        ProductId INT  AUTO_INCREMENT PRIMARY KEY,
                        Nom VARCHAR(30) NOT NULL,
                        Detail VARCHAR(255) NOT NULL,
                        Stock INT NOT NULL,
                        Price FLOAT NOT NULL)";
                
                $dbco->exec($sql);
                echo 'Table bien créée !';
            }
            
            catch(PDOException $e){
              echo "Erreur : " . $e->getMessage();
            }
        ?>
