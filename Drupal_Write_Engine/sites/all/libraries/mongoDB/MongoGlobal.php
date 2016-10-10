<?php
/**
 * @file MongoGlobal Class file to interface with MongoDB
 *
 */


class MongoGlobal
{

	//the db host
	private $mongo_db_host = '';
	//the db name
	private $mongo_db_name = '';
	//the db user on the database
	private $mongo_user = '';
	//the db password for the above user on the database
	private $mongo_password = '';
	//the db object
	private $db;

	

	function __construct($host, $db_name, $user, $password) {
		
		if(!empty($user) && !empty($password)){
			$this->mongo_db_host = $host;
			$this->mongo_db_name = $db_name;
			$this->mongo_user = $user;
			$this->mongo_password = $password;

			$m = new MongoClient("mongodb://$this->mongo_user:$this->mongo_password@$this->mongo_db_host:27017/$this->mongo_db_name");
		}else{
			$this->mongo_db_host = $host;
			$this->mongo_db_name = $db_name;
			$m = new MongoClient("mongodb://$this->mongo_db_host");
		}
		$this->db = $m->drupal_uk_mongo;
	}

	public function insert_one_or_many_nodes($nodes, $type){

		$count = count($nodes);
		$i = 0;

		if($count > 0){
			
			$nodes_collection;
			// Get the question collection
			if($type == 'question'){
				$nodes_collection = $this->db->questions;
			//get the challenge collection
			}else if($type == 'challenge'){
				$nodes_collection = $this->db->challenge;
			}

			//try and save the node data
			foreach ($nodes as $key => $value) {
				try{
					$nodes_collection->save($value);
					$i++;
				}catch(Exception $e){
					return FALSE;
				}
			}
			if($i == $count){
				return TRUE;
			}else{
				return FALSE;
			}
		}
	}

	/**
	 *  Function that deletes nodes
	 **/
	public function delete_existing_node($nid, $type){
		
		$nodes_collection;
		// Get the question collection
		if($type == 'question'){
			$nodes_collection = $this->db->questions;
		}else if($type == 'challenge'){
			$nodes_collection = $this->db->challenges;
		}

		//try and delete a document.
		try{
			$nodes_collection->remove(array("nid" => $nid), array("justOne" => true));
		}catch(Exception $e){
			return FALSE;
		}
		return TRUE;
	}

	/**
	 *  Function that specifically updates existing or adds new nodes
	 **/
	public function add_or_update_node($data, $nid, $type){

		$nodes_collection;
		// Get the question collection
		if($type == 'question'){
			$nodes_collection = $this->db->questions;
		}else if($type == 'challenge'){
			$nodes_collection = $this->db->challenges;
		}

		//try and update a document.
		//if the document does not exist then a new one is created using the upsert flag
		try{
			$nodes_collection->update(array("nid" => $nid), $data, array("upsert" => true));
		}catch(Exception $e){
			return FALSE;
		}
		return TRUE;
	}

	/**
	 *  Function that specifically updates or adds new leaderboard data
	 **/
	public function add_or_update_leaderboard($data){

		$nodes_collection = $this->db->leaderboards;
		//try and update a document.
		//if the document does not exist then a new one is created using the upsert flag
		try{
			$nodes_collection->update(array("title" => 'Leaderboard'), $data, array("upsert" => true));
		}catch(Exception $e){
			return FALSE;
		}
		return TRUE;
	}

	/**
	 *  Function that specifically updates existing or adds new nodes
	 **/
	public function add_or_update_user($data, $uid){

		// Get the users collection
		$nodes_collection = $this->db->users;

		//try and update a document.
		//if the document does not exist then a new one is created using the upsert flag
		try{
			$nodes_collection->update(array("uid" => $uid), $data, array("upsert" => true));
		}catch(Exception $e){
			return FALSE;
		}
		return TRUE;
	}
	
}