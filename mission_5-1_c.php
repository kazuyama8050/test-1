<!DOCTYPE html>
<html lang="ja">
    
    <head>
        <meta charset="utf-8">
        <title>mission_5-1</title>
    </head>
    
    <body>
        <form method="POST" action="mission_5-1.php">
            <input type="name" name="name" placeholder="名前">
            <input type="text" name="text" placeholder="コメント">
            <input type="text" name="pass" placeholder="パスワード">
            <input type="submit" name="submit">
            
        </form>
        
        <form method="POST" action="mission_5-1.php">
            <input type="number" name="number" placeholder="削除番号">
            <input type="text" name="pass_d" placeholder="パスワード">
            <input type="submit" name="delete" value="削除">
        </form>
        
        <form method="POST" action="mission_5-1.php">
                <input type="number" name="change_number" placeholder="編集番号">
                <input type="text" name="text_c" placeholder="編集コメント">
                <input type="text" name="pass_c" placeholder="パスワード">
                <input type="submit" name="change" value="編集">
        </form>
        
        <?php
            $dsn="mysql:dbname=xxxx;host=localhost";
            $user="xxxx";
            $password="xxxx";
            $pdo=new PDO($dsn,$user,$password,array(PDO::ATTR_ERRMODE=>PDO::ERRMODE_WARNING));
            
            $sql="CREATE TABLE IF NOT EXISTS tb51"
            ."("
            . "id INT AUTO_INCREMENT PRIMARY KEY,"
            . "name char(32),"
            . "comment TEXT,"
            . "password TEXT"
            .");";
            $stmt=$pdo->query($sql);
            
            
        ?>
  
        <?php
            $date=date("Y/m/d H:i:s");
            if (isset($_POST["name"])&&$_POST["name"]!=""&&
            isset($_POST["text"])&&$_POST["text"]!=""&&
            isset($_POST["pass"])&&$_POST["pass"]!=""){
                $name=$_POST["name"];
                $text=$_POST["text"];
                $pass=$_POST["pass"];
                if ($text!="" && $pass!=""){
                    $sql=$pdo->prepare("INSERT INTO tb51 (name,comment,password) VALUES (:name, :text, :pass)");
                    $sql->bindParam(":name", $name, PDO::PARAM_STR);
                    $sql->bindParam(":text", $text, PDO::PARAM_STR);
                    $sql->bindParam(":pass", $pass, PDO::PARAM_STR);
                    $sql->execute();
                
                    $sql="SELECT * FROM tb51";
                    $stmt=$pdo->query($sql);
                    $results=$stmt->fetchAll();
                    foreach ($results as $row){
                        echo $row["id"].",";
                        echo $row["name"].",";
                        echo $row["comment"]."<br>";
        
                    echo "<hr>";
                    }
                }
            }
        ?>
        
        <?php
            if (isset($_POST["number"])&&$_POST["number"]!=""&&
            isset($_POST["pass_d"])&&$_POST["pass_d"]!=""){
                $delete=$_POST["number"];
                $delete=intval($delete);
                $pass_d=$_POST["pass_d"];
                if ($delete != "" && $pass_d != ""){
                            
                    $sql="delete from tb51 where id=:delete AND password=:pass_d";
                    $stmt=$pdo->prepare($sql);
                    $stmt->bindParam(":delete",$delete,PDO::PARAM_INT);
                    $stmt->bindParam(":pass_d",$pass_d,PDO::PARAM_STR);
                    $stmt->execute();
                    
                    $sql="SELECT * FROM tb51";
                    $stmt=$pdo->query($sql);
                    $results=$stmt->fetchAll();
                    foreach ($results as $row){
                        echo $row["id"].",";
                        echo $row["name"].",";
                        echo $row["comment"]."<br>";
        
                    echo "<hr>";
                    }
                                
                }
            }
        ?>
        <?php
            if (isset($_POST["change_number"])&&$_POST["change_number"]!=""&&
            isset($_POST["text_c"])&&$_POST["text_c"]!=""&&
            isset($_POST["pass_c"])&&$_POST["pass_c"]!=""){
                $change_n=$_POST["change_number"];
                $change_n=intval($change_n);
                $text_c=$_POST["text_c"];
                $pass_c=$_POST["pass_c"];
                if ($change_n!="" && $pass_c!=""){
                    $sql = 'UPDATE tb51 SET comment=:text_c WHERE id=:change_n AND password=:pass_c';
	                $stmt = $pdo->prepare($sql);
	                $stmt->bindParam(':text_c', $text_c, PDO::PARAM_STR);
	                $stmt->bindParam(':pass_c', $pass_c, PDO::PARAM_STR);
	                $stmt->bindParam(':change_n', $change_n, PDO::PARAM_INT);
	                $stmt->execute();
	                
	                $sql="SELECT * FROM tb51";
                    $stmt=$pdo->query($sql);
                    $results=$stmt->fetchAll();
                    foreach ($results as $row){
                        echo $row["id"].",";
                        echo $row["name"].",";
                        echo $row["comment"]."<br>";
        
                    echo "<hr>";
                    }
                }
            }
        ?>
        
    </body>
</html>